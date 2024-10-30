from flask import Blueprint, request, jsonify, flash, redirect, url_for, render_template
from .forms import ProductForm
from models.product import Product  # Assuming you have a Product model
import paypalrestsdk

farmer_bp = Blueprint('farmer_routes', __name__)

# Configure the PayPal SDK
paypalrestsdk.configure({
    "mode": "sandbox",  # or "live"
    "client_id": "Acwg4xRrxtXPMPxbRzvodfjreL9TdB8lG51Hq3TUrMH2mEKY7gLLFC8nzAHrkcoH534yGCXZbf6gu6-X",
    "client_secret": "EId1pe2UtS7d7ZCjyQD6Rde-BkuiR88GHc9o1Q4cc3pbRm9uDhkFhayAhORY0WdWziTGZw6AjRRUeHQJ"
})


@farmer_bp.route('/create_payment/<int:product_id>', methods=['POST'])
def create_payment(product_id):
    # Retrieve product details from the database using product ID
    product = Product.query.get(product_id)
    if product is None:
        flash("Product not found", "error")
        return redirect(url_for('farmer_routes.farmer_profile'))

    # Create PayPal payment object
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": url_for('farmer_routes.payment_success', _external=True),
            "cancel_url": url_for('farmer_routes.payment_cancel', _external=True)
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": product.name,
                    "sku": str(product.id),
                    "price": str(product.price),
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": str(product.price),
                "currency": "USD"
            },
            "description": f"Payment for {product.name}"
        }]
    })

    # Attempt to create the payment
    if payment.create():
        # Redirect to PayPal for payment approval
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)  # Redirects to PayPal payment page
    else:
        flash("Payment creation failed. Please try again.", "error")
        return redirect(url_for('farmer_routes.farmer_profile'))

@farmer_bp.route('/farmer/profile', methods=['GET', 'POST'])
def farmer_profile():
    # Logic for farmer profile here
    return render_template('farmer_profile.html')


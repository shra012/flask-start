from flask import render_template, redirect, url_for
from flask_login import login_required

from .mobile_controller import cart_items
from . import cart_controller


@cart_controller.route("/")
@login_required
def cart():
    return render_template("cart.html", cart_items=cart_items, len=len)


@cart_controller.route("/deleteItem/<int:id>")
@login_required
def delete_item(id):
    for index, cart_item in enumerate(cart_items):
        if cart_item.id == id:
            del cart_items[index]
    return redirect(url_for('cart_controller.cart'))

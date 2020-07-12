from flask import render_template, abort, redirect, url_for, request
from flask_login import login_required

from ..model.model import Item

from . import mobile_controller

cart_items = []


@mobile_controller.route("/<int:id>")
def mobile(id):
    try:
        toast = False
        if len(request.args) > 0:
            toast = request.args['toast']
        item = Item.query.get(id)
        return render_template("mobile.html", item=item, toast=toast)
    except Exception as e:
        print(e)
        abort(404)


@mobile_controller.route("/buynow/<int:id>")
@login_required
def buynow(id):
    item = Item.query.get(id)
    cart_items.append(item)
    return redirect(url_for('cart_controller.cart'))


@mobile_controller.route("/addtocart/<int:id>")
@login_required
def add_to_cart(id):
    item = Item.query.get(id)
    cart_items.append(item)
    return redirect(url_for('mobile_controller.mobile', id=id, toast=True))

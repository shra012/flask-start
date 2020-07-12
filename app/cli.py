from .model.model import Item, db


def add_cli_methods(app):
    @app.cli.command("init_db")
    def init_db():
        """ 
        Initialize the tables of this application
        """
        try:
            db.create_all()
            print("Created all the tables")
        except Exception as e:
            print(e)

    @app.cli.command("load_data")
    def load_data():
        """ 
        Load the dummy data 
        """
        item1 = Item(item_type="Smart Phone", item_name="SAMSUNG Galaxy 10",
                     item_description="A Samsung Branded Galaxy Flagship Phone",
                     item_details="THE MOST POWERFULL CAMERA", item_image_name="samsung_galaxy_10.jpg")
        db.session.add(item1)
        item2 = Item(item_type="Smart Phone", item_name="One Plus 7 Pro",
                     item_description="A One Plus Branded Top Smart Phone",
                     item_details="FLUID DYNAMIC DISPLAY", item_image_name="one_plus_7_pro.jpg")
        db.session.add(item2)
        item3 = Item(item_type="Smart Phone", item_name="Huawei Y9 Prime",
                     item_description="A Huawei Branded Top Smart Phone",
                     item_details="4000 MAH BATTERY", item_image_name="huawei_y9_prime.jpg")
        db.session.add(item3)
        item4 = Item(item_type="Smart Phone", item_name="Oppo Reno",
                     item_description="A Oppo Reno Branded Top Smart Phone",
                     item_details="THE POWERFULL PROCESSOR", item_image_name="oppo_reno.jpg")
        db.session.add(item4)
        item5 = Item(item_type="Smart Phone", item_name="SAMSUNG Galaxy 10+",
                     item_description="A Samsung Branded Galaxy Flagship Phone",
                     item_details="6.1\" AMOLED DISPLAY", item_image_name="samsung_galaxy_10_plus.jpg")
        db.session.add(item5)
        item6 = Item(item_type="Smart Phone", item_name="One Plus 7T Pro",
                     item_description="A One Plus Branded Top Smart Phone",
                     item_details="TRIPLE CAMERA AT ITS BEST", item_image_name="one_plus_7t_pro.jpg")
        db.session.add(item6)
        item7 = Item(item_type="Smart Phone", item_name="iPhone Xs Max",
                     item_description="A Apple Branded Top iPhone",
                     item_details="WIRELESS CHARGING WITH ALL QI CHARGERS", item_image_name="iphone_xs_max.jpg")
        db.session.add(item7)
        item8 = Item(item_type="Smart Phone", item_name="Redmi Note 9 PRO",
                     item_description="A Xaiomi Branded Top Smart Phone",
                     item_details="QUALCOMM SNAPDRAGON 720G", item_image_name="redmi_note_9_pro.jpg")
        db.session.add(item8)
        item9 = Item(item_type="Smart Phone", item_name="One Plus 8 Series 5G",
                     item_description="A One Plus Branded Top Smart Phone",
                     item_details="ULTRA FAST SNAPDRAGON 865", item_image_name="one_plus_8.jpg")
        db.session.add(item9)
        item10 = Item(item_type="Smart Phone", item_name="One Plus 7T",
                      item_description="A One Plus Branded Top Smart Phone",
                      item_details="POP UP CAMERA", item_image_name="one_plus_7t.jpg")
        db.session.add(item10)
        item11 = Item(item_type="Smart Phone", item_name="SAMSUNG Galaxy Z flip",
                      item_description="A Samsung Branded Galaxy Flagship Phone",
                      item_details="6.7\" FOLDABLE FLIP SMARTPHONE", item_image_name="samsung_galaxy_z_flip.jpg")
        db.session.add(item11)
        item12 = Item(item_type="Smart Phone", item_name="Redmi Note 9 Pro Max",
                      item_description="A Xaiomi Branded Top Smart Phone",
                      item_details="64 MP QUAD CAMERA", item_image_name="redmi_note_9_pro_max.jpg")
        db.session.add(item12)
        db.session.commit()

    @app.cli.command("drop_db")
    def drop_db():
        """
        Drops all tables of this application
        """
        try:
            db.drop_all()
            print("Dropped all the tables")
        except Exception as e:
            print(e)

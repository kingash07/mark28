from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/")
def home():
    return render_template("home.html")

# name of the website
# -------------------
# GleamingGems
# LuminaryLuxury
# JeweledHaven
# OrnateOpulence
# EnchantingTrinkets
# SparklingSplendor
# PreciousCharm
# RegalAdornments
# GlamorousGleam
# ShimmeringJewels
# --------------------


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

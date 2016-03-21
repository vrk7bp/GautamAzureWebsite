"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject import app

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html'
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )

@app.route('/aboutme')
def aboutMe():
	return render_template('AboutMe.html')

@app.route('/nasa')
def nasa():
	return redirect("http://www.seas.virginia.edu/pubs/spectra/pdfs/nasapartnerships.pdf", code=302)

@app.route('/resume')
def resume():
	return redirect("https://s3.amazonaws.com/GautamResume/GautamKanumuruResume.pdf", code=302)

@app.route('/uvradiationabstract')
def uvabstract():
	return redirect("https://s3.amazonaws.com/GautamResume/UVAbstract.pdf", code=302)

@app.route('/uvradiationpaper')
def uvpaper():
	return redirect("https://s3.amazonaws.com/GautamResume/UVPaper.pdf", code=302)

@app.route('/fieabstract')
def fieabstract():
	return redirect("https://s3.amazonaws.com/GautamResume/FIEAbstract.pdf", code=302)

@app.route('/fiepaper')
def fiepaper():
	return redirect("https://s3.amazonaws.com/GautamResume/FIEPaper.pdf", code=302)

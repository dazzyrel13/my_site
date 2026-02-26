from flask import Flask, render_template

app = Flask(__name__)

# Главная
@app.route('/')
def index():
    return render_template('index.html', active_page='index')

# Легковые
@app.route('/cars')
def cars():
    return render_template('cars.html', active_page='cars')

@app.route('/cars/new')
def cars_new():
    return render_template('cars_new.html', active_page='cars_new')

@app.route('/cars/used')
def cars_used():
    return render_template('cars_used.html', active_page='cars_used')

# Подробные страницы
@app.route('/car/honda-fit')
def car_honda_fit():
    return render_template('car_honda_fit.html', active_page='car_honda_fit')

@app.route('/car/audi-q7')
def car_audi_q7():
    return render_template('car_audi_q7.html', active_page='car_audi_q7')

@app.route('/car/mazda-mx5')
def car_mazda_mx5():
    return render_template('car_mazda_mx5.html', active_page='car_mazda_mx5')

# Тягачи
@app.route('/car/foton-galaxy')
def car_foton_galaxy():
    return render_template('car_foton_galaxy.html', active_page='car_foton_galaxy')

# Грузовые
@app.route('/trucks')
def trucks():
    return render_template('trucks.html', active_page='trucks')

@app.route('/trucks/tractors')
def trucks_tractors():
    return render_template('trucks_tractors.html', active_page='trucks_tractors')

@app.route('/trucks/dumpers')
def trucks_dumpers():
    return render_template('trucks_dumpers.html', active_page='trucks_dumpers')

@app.route('/trucks/trucks')
def trucks_trucks():
    return render_template('trucks_trucks.html', active_page='trucks_trucks')

@app.route('/trucks/vans')
def trucks_vans():
    return render_template('trucks_vans.html', active_page='trucks_vans')

@app.route('/trucks/km')
def trucks_km():
    return render_template('trucks_km.html', active_page='trucks_km')

@app.route('/trucks/evac')
def trucks_evac():
    return render_template('trucks_evac.html', active_page='trucks_evac')

# Спецтехника
@app.route('/special')
def special():
    return render_template('special.html', active_page='special')

@app.route('/special/lifts')
def special_lifts():
    return render_template('special_lifts.html', active_page='special_lifts')

@app.route('/special/frontal')
def special_frontal():
    return render_template('special_frontal.html', active_page='special_frontal')

@app.route('/special/forklift')
def special_forklift():
    return render_template('special_forklift.html', active_page='special_forklift')

@app.route('/special/excavators')
def special_excavators():
    return render_template('special_excavators.html', active_page='special_excavators')

# Контакты
@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request
import utils
app = Flask(__name__) 

@app.route('/') 
def home(): 
    return render_template('index.html')

@app.route('/predict/', methods=['GET', 'POST']) 
def predict(): 
    if request.method == 'POST': 
        Period_of_stay = request.form.get('Period_of_stay')
        print(Period_of_stay)
        Traveler_type = request.form.get('Traveler_type')
        print(Traveler_type)
        Pool = request.form.get('Pool')
        print(Pool)
        Gym = request.form.get('Gym')
        print(Gym) 
        Tennis_court = request.form.get('Tennis_court')
        print(Tennis_court)
        Spa = request.form.get('Spa')
        print(Spa)
        Casino = request.form.get('Casino')
        print(Casino)
        Free_internet = request.form.get('Free_internet')
        print(Free_internet)
        Hotel_stars = request.form.get('Hotel_stars')
        print(Hotel_stars)
        Member_years = request.form.get('Member_years')
        print(Member_years)
        Review_month = request.form.get('Review_month')
        print(Review_month)
        Review_weekday = request.form.get('Review_weekday')
        print(Review_weekday)

    prediction = utils.preprocessdata(Period_of_stay,Traveler_type,Pool,Gym,Tennis_court,Spa,Casino,Free_internet,Hotel_stars,Member_years,Review_month,Review_weekday) 

    return render_template('predict.html', prediction=prediction) 
if __name__ == '__main__': 
    app.run(debug=True)
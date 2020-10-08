from flask import Flask, request, jsonify, render_template
import pickle
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Pickle_LGBM_Model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Estimated_insects=float(request.form['Estimated Insects Count'])
        Doses_per_week=int(request.form['Number of Doses per week'])
        no_weeks_used=float(request.form['Number of weeks used'])
        no_weeks_quit = float(request.form['Number of Weeks quit'])
        Crop_type=request.form['Crop Type']
        if(Crop_type=='Type 0'):
            Crop_type=0
        elif(Crop_type == 'Type 1'):
            Crop_type =1

        Soil = request.form['Soil Type']
        if (Soil == 'Type 0'):
            Soil = 0
        elif (Soil == 'Type 1'):
            Soil = 1

        Pesticides_usage = request.form['Pesticides Usage']
        if (Pesticides_usage == 'Never Used'):
            Pesticides_usage = 0
        elif (Pesticides_usage == 'Previously Used'):
            Pesticides_usage = 1


        Season = request.form['Season']
        if (Season == 'Season Type 1'):
            Season = 0
        elif (Season == 'Season Type 2'):
            Season = 1
        elif (Season == 'Season Type 2'):
            Season = 2

        Avg_Dose_Insect = float(Estimated_insects / Doses_per_week)
        TotalDoses = float(Doses_per_week * no_weeks_used)

        prediction=model.predict([[Estimated_insects,Crop_type,Soil,Pesticides_usage,Doses_per_week,no_weeks_used,no_weeks_quit,Season,Avg_Dose_Insect,TotalDoses]])
        if prediction == 0:
            output="Crop will be alive"
        elif prediction == 1:
            output="Crop is likely to get spoiled"
        else:
            output = "Crop will get spoiled due to pesticides"


        return render_template('index.html', prediction_crop_damage='{}'.format(output))


if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000,debug=True,use_reloader=True)

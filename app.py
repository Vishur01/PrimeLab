from flask import Flask, render_template, request, redirect, url_for
import pickle
import numpy as np

app = Flask(__name__, template_folder='template')

# Load the models

C1 = pickle.load(open('C1.pkl', 'rb'))
C2 = pickle.load(open('C2.pkl', 'rb'))
C3 = pickle.load(open('C3.Pkl', 'rb'))
C4 = pickle.load(open('C4.pkl', 'rb'))
C5 = pickle.load(open('C5.pkl', 'rb'))
C6 = pickle.load(open('C6.pkl', 'rb'))

P1 = pickle.load(open('P1.pkl', 'rb'))
P2 = pickle.load(open('P2.pkl', 'rb'))
P3 = pickle.load(open('P3.Pkl', 'rb'))
P4 = pickle.load(open('P4.pkl', 'rb'))
P5 = pickle.load(open('P5.pkl', 'rb'))
P6 = pickle.load(open('P6.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_model = request.form['model_select']
        if selected_model == 'C1':
            return redirect(url_for('input_page1', model='C1'))
        elif selected_model == 'C2':
            return redirect(url_for('input_page2', model='C2'))
        elif selected_model == 'C3':
            return redirect(url_for('input_page3', model='C3'))
        elif selected_model == 'C4':
            return redirect(url_for('input_page4', model='C4'))
        elif selected_model == 'C5':
            return redirect(url_for('input_page5', model='C5'))
        elif selected_model == 'C6':
            return redirect(url_for('input_page6', model='C6'))
        
        elif selected_model == 'P1':
            return redirect(url_for('input_page1', model='P1'))
        elif selected_model == 'P2':
            return redirect(url_for('input_page2', model='P2'))
        elif selected_model == 'P3':
            return redirect(url_for('input_page3', model='P3'))
        elif selected_model == 'P4':
            return redirect(url_for('input_page4', model='P4'))
        elif selected_model == 'P5':
            return redirect(url_for('input_page5', model='P5'))
        elif selected_model == 'P6':
            return redirect(url_for('input_page6', model='P6'))
        
    return render_template('index.html')

#Input page 1

@app.route('/input_page1/<model>', methods=['GET', 'POST'])
def input_page1(model):
    predC1, predP1 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Abrasion_value']
        viscosity = float(request.form['ZSV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C1':
            predC1 = C1.predict(input_data)
            predC1 = [f"{float(predC1)-2:.2f}", f"{float(predC1)+2:.2f}"]
        elif model == 'P1':
            predP1 = P1.predict(input_data)
            predP1 = [f"{float(predP1)-2:.2f}", f"{float(predP1)+2:.2f}"]
        
    return render_template('input_page1.html', model=model, predC1=predC1, predP1=predP1)

#Input page 2

@app.route('/input_page2/<model>', methods=['GET', 'POST'])
def input_page2(model):
    predC2, predP2 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Impact_Value']
        viscosity = float(request.form['ZSV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C2':
            predC2 = C2.predict(input_data)
            predC2 = [f"{float(predC2)-2:.2f}", f"{float(predC2)+2:.2f}"]
        elif model == 'P1':
            predP2 = P2.predict(input_data)
            predP2 = [f"{float(predP2)-2:.2f}", f"{float(predP2)+2:.2f}"]
        
    return render_template('input_page2.html', model=model, predC2=predC2, predP2=predP2)

#Input page 3

@app.route('/input_page3/<model>', methods=['GET', 'POST'])
def input_page3(model):
    predC3, predP3 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Specific Gravity']
        viscosity = float(request.form['ZSV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C3':
            predC3 = C3.predict(input_data)
            predC3 = [f"{float(predC3)-2:.2f}", f"{float(predC3)+2:.2f}"]
        elif model == 'P3':
            predP3 = P3.predict(input_data)
            predP3 = [f"{float(predP3)-2:.2f}", f"{float(predP3)+2:.2f}"]
        
    return render_template('input_page3.html', model=model, predC3=predC3, predP3=predP3)

#Input page 4

@app.route('/input_page4/<model>', methods=['GET', 'POST'])
def input_page4(model):
    predC4, predP4 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Abrasion_value']
        viscosity = float(request.form['KV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C4':
            predC4 = C4.predict(input_data)
            predC4 = [f"{float(predC4)-2:.2f}", f"{float(predC4)+2:.2f}"]
        elif model == 'P4':
            predP4 = P4.predict(input_data)
            predP4 = [f"{float(predP4)-2:.2f}", f"{float(predP4)+2:.2f}"]
        
    return render_template('input_page4.html', model=model, predC4=predC4, predP4=predP4)

#Input page 5

@app.route('/input_page5/<model>', methods=['GET', 'POST'])
def input_page5(model):
    predC5, predP5 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Impact_Value']
        viscosity = float(request.form['KV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C5':
            predC5 = C5.predict(input_data)
            predC5 = [f"{float(predC5)-2:.2f}", f"{float(predC5)+2:.2f}"]
        elif model == 'P5':
            predP5 = P5.predict(input_data)
            predP5 = [f"{float(predP5)-2:.2f}", f"{float(predP5)+2:.2f}"]
        
    return render_template('input_page5.html', model=model, predC5=predC5, predP5=predP5)

#Input page 6

@app.route('/input_page6/<model>', methods=['GET', 'POST'])
def input_page6(model):
    predC6, predP6 = None, None
    
    if request.method == 'POST':
        aggregate = request.form['Aggregate']
        source = request.form['Specific Gravity']
        viscosity = float(request.form['KV'])  # Assuming viscosity is a float
        dag = request.form['DAG']
        air_voids = request.form['air_voids']
        
        # Convert input data to a format that the model expects
        input_data = np.array([[aggregate, source, viscosity, dag, air_voids]])
        
        # Make prediction using the selected model
        if model == 'C6':
            predC6 = C6.predict(input_data)
            predC6 = [f"{float(predC6)-2:.2f}", f"{float(predC6)+2:.2f}"]
        elif model == 'P6':
            predP6 = P6.predict(input_data)
            predP6 = [f"{float(predP6)-2:.2f}", f"{float(predP6)+2:.2f}"]
        
    return render_template('input_page6.html', model=model, predC6=predC6, predP6=predP6)

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, request, render_template, flash, redirect
import requests, json, sys, os


app = Flask(__name__)
app.secret_key = 'khoikhukho'

@app.route('/')
def form():
    return render_template('home.html')

@app.route('/flat-file-insert')
def flat_file_insert():
    return render_template('flat_file_insert.html')

@app.route('/send-email-notification')
def send_email_notification():
    return render_template('send-email-notification.html')
 
@app.route('/data/', methods = ['POST', 'GET'])
def data():
    if request.method == 'GET':
        return f"The URL /data is accessed directly. Try going to '/form' to submit form"
    if request.method == 'POST':
        form_data = request.form
        print(form_data['Name'])
        return render_template('data.html',form_data = form_data)

@app.route('/upload-email-address', methods=['POST'])
def upload_email_address(): 
    if request.method == 'POST':
     
        # sampling_rate = int(request.values.get('sr'))
        name_subject = str(request.values.get('subjectname'))
        print(name_subject)
        headers = {"Content-type": "application/json"}
        data ={"email": "{}".format(name_subject)}
        r = requests.post(url = "https://prod-17.southeastasia.logic.azure.com:443/workflows/e26f2a5c788449bc8e8cccdaf1495b93/triggers/manual/paths/invoke?api-version=2016-10-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=O_y1Ye0U6HoJ5l02zHshv62d9o4rqHi0p9fQa6t8iLw", data=json.dumps(data), headers = headers)
        flash(f'{r.text}', 'success')


    return redirect('/send-email-notification')


if __name__ == "__main__":
    app.run(host="0.0.0.0",port=8000,debug=True,threaded=True)
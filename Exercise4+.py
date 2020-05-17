from flask import Flask, request

app = Flask(__name__)

HTML = """<html>
<head>
<title>
</title>
</head>
<body>
    <h1>Think of a number between 0 and 1000 </h1>
    <form method='post'>
    <input type='hidden' name='min' value='{}'>
    <input type='hidden' name='max' value='{}'>
    <input type='submit' value='START'>
    </form>
</body>
</html>"""

HTML2 = """<html>
<head>
<title>
</title>
</head>
<body>
    <h1>Is this: {guess} your number?</h1>
    <form method='post'>
    <input type='submit' name='answer' value='too small'>
    <input type='submit' name='answer' value='too big'>
    <input type='submit' name='answer' value='you win'>
    <input type='hidden' name='min' value='{min_number}'>
    <input type='hidden' name='max' value='{max_number}'>
    <input type='hidden' name='guess' value='{guess}'>

    </form>
</body>
</html>"""

HTML3 = """<html>
<head>
<title>WIN
</title>
</head>
<body>
<h1>Hooray! I've won! Your number is: {guess}</h1>
</body></html>"""


@app.route('/guess', methods=['GET', 'POST'])
def guess():
    """
    Website guesses user's number.
    User gives website hints.

    :return: website with current guess
    """
    if request.method == 'GET':
        return HTML.format(0, 1000)
    else:
        min_number = int(request.form.get('min'))
        max_number = int(request.form.get('max'))
        guess = int(request.form.get('guess', 500))
        user_choice = request.form.get('answer')
        if user_choice == 'too small':
            min_number = guess
        elif user_choice == 'too big':
            min_number = guess
        elif user_choice == 'you win':
            return HTML3.format(guess=guess)

        guess = (max_number - min_number) // 2 + min_number

        return HTML2.format(guess=guess, min_number=min_number, max_number=max_number)


if __name__ == '__main__':
    app.run(debug=True)

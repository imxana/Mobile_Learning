from flask import request, jsonify, g


def register(app):

    @app.route('/')
    def show_root():
        return 'This is ./'
   

    @app.route('/signin', methods=['POST'])
    def signin():
        error = None
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        user = g.User.query.filter_by(username=username).first()
        if not bool(user):
            error = 'Invalid username'
        elif password != user.password:
            error = 'Invalid password'

        if bool(error):
            return jsonify({'code':0, 'error':error})

        return jsonify({'code':1})


    @app.route('/signup', methods=['POST'])
    def signup():
        error = None
        username = request.form.get('username', '')
        password = request.form.get('password', '')
        email = request.form.get('email', '')
            
        user = g.User.query.filter_by(username=username).first()

        if bool(user):
            return jsonify({'code':0, 'error':'Invalid username'})

        new_user = g.User(username, email, password)
        try:
            g.db.session.add(new_user)
            g.db.session.commit()
        except Exception:
            g.db.session.rollback()
            error = 'SQL failed'

        if bool(error):
            return jsonify({'code':0, 'error':error})

        return jsonify({'code':1})
    

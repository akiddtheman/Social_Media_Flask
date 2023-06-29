from database.models import User, Password, db

# Регистрация пользователя
def register_user_db(**user_data):
    new_user = User(**user_data)
    db.session.add(new_user)
    db.session.commit()


# Проверка пользователя по email
def check_user_db(email):
    user = User.query.filter_by(email=email).first()
    if user:
        return True
    else:
        return False


# Проверка пароля пользователя
def check_user_password_db(email, password):
    user = User.query.filter_by(email=email).first()
    if user:
        user_password = Password.query.filter_by(user_id=user.id).first()
        if user_password and user_password.check_password(password):
            return True
    return False


# Получение всех пользователей из базы
def get_all_users_db():
    users = User.query.all()
    return users


# Получить конкретного пользователя
def get_exact_users_db(user_id):
    exact_user = User.query.filter_by(user_id=user_id).first()
    return exact_user


# Удалить пользователя из базы
def delete_user_db(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if user:
        db.session.delete(user)
        db.session.commit()

        return True

    return False
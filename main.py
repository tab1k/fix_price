# try / except - это конструкция для обработки ошибок. 

# Она позволяет программе продолжать работу, даже если возникает ошибка.



def fetch_user_data(user_id):
    
    print(f"Ищем данные для пользователя {user_id}...")
    
    try:
        print(f'Подключаемся к БД и ищем пользователя с id {user_id}...')
        if user_id < 0:
            raise ValueError("ID пользователя не может быть отрицательным!")
    
        user_data = {"id": user_id, "name": "Tabik"}
        
    except TypeError as e:
        print(f"Ошибка! Неверный тип данных: {e}")
        
    except ValueError as e:
        print(f"Ошибка! Неверные данные: {e}")
        
    else:
        print(f"Данные пользователя: {user_data}")
    
    finally:
        print("Завершение операции.\n")
        
        
fetch_user_data('1')
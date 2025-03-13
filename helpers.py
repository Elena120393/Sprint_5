
import uuid

def generate_unique_email(domain="example.com"):
    """
    Генерирует уникальный email адрес с использованием случайного UUID.
    :param domain: Домен для email, по умолчанию "example.com".
    :return: Уникальный email адрес.
    """
    unique_str = uuid.uuid4().hex[:8]
    return f"test_{unique_str}@{domain}"

if __name__ == "__main__":
    # Пример использования
    print(generate_unique_email("gmail.com"))

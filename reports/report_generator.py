import allure
import os


class ReportGenerator:

    @staticmethod
    def log_test_step(description: str):
        """
        Логирует шаг теста в отчет Allure.

        :param description: Описание шага.
        """
        allure.attach(description, name="Test Step", attachment_type=allure.attachment_type.TEXT)

    @staticmethod
    def log_test_result(result: bool, attachment: bytes = None):
        """
        Логирует результат теста в отчет Allure.

        :param result: Результат теста (True - успешно, False - провалено).
        :param attachment: Вложение (например, скриншот) для прикрепления к отчету.
        """
        allure.attach(attachment, "Screenshot", allure.attachment_type.PNG)
        assert result, "Test failed: check attached screenshot"

    @staticmethod
    def generate_allure_report():
        """
        Генерирует отчет Allure и открывает его в браузере.
        """
        allure_cmd = "allure serve allure-results"
        os.system(allure_cmd)

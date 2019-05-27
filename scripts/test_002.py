import allure


class Test002:
    def test_add_png(self):
        with open("C:\\Users\\居居\Desktop\\APP08\\scripts\\abc.png", "rb") as f:
            allure.attach("截图", f.read(), allure.attach_type.PNG)

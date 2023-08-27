from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class PriceCalculatorApp(App):
    def build(self):
        self.title = "BWD Cu.M. Calculator"
        layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        # Labels and Entry Fields
        layout.add_widget(Label(text="Base:"))
        self.base_entry = TextInput()
        layout.add_widget(self.base_entry)

        layout.add_widget(Label(text="11-20:"))
        self.first_range_entry = TextInput()
        layout.add_widget(self.first_range_entry)

        layout.add_widget(Label(text="21-30:"))
        self.second_range_entry = TextInput()
        layout.add_widget(self.second_range_entry)

        layout.add_widget(Label(text="31-40:"))
        self.third_range_entry = TextInput()
        layout.add_widget(self.third_range_entry)

        layout.add_widget(Label(text="41 and above:"))
        self.fourth_range_entry = TextInput()
        layout.add_widget(self.fourth_range_entry)

        layout.add_widget(Label(text="Present Value (in cubic meter):"))
        self.present_entry = TextInput()
        layout.add_widget(self.present_entry)

        layout.add_widget(Label(text="Previous Value (in cubic meter):"))
        self.previous_entry = TextInput()
        layout.add_widget(self.previous_entry)

        # Calculate Button
        calculate_button = Button(text="Calculate")
        calculate_button.bind(on_release=self.calculate_price)
        layout.add_widget(calculate_button)

        # Result Label
        self.result_label = Label(text="")
        layout.add_widget(self.result_label)

        return layout

    def calculate_price(self, instance):
        present_value = int(self.present_entry.text)
        previous_value = int(self.previous_entry.text)
        base_value = int(self.base_entry.text)
        firstRangeValue = int(self.first_range_entry.text)
        secondRangeValue = int(self.second_range_entry.text)
        thirdRangeValue = int(self.third_range_entry.text)
        fourthRangeValue = int(self.fourth_range_entry.text)
        volume = present_value - previous_value

        if volume >= 41:
            price = fourthRangeValue * (volume - 40) + (thirdRangeValue * 10) + (secondRangeValue * 10) + (base_value + (firstRangeValue * 10))
        elif volume >= 31:
            price = thirdRangeValue * (volume - 30) + (secondRangeValue * 10) + (base_value + (firstRangeValue * 10))
        elif volume >= 21:
            price = secondRangeValue * (volume - 20) + (base_value + (firstRangeValue * 10))
        elif volume >= 11:
            price = base_value + (firstRangeValue * (volume - 10))
        else:
            price = base_value

        self.result_label.text = f"Price: {price} PHP"

if __name__ == '__main__':
    PriceCalculatorApp().run()

class Stock:
    __slots__ = ["name", "open_price", "current_price", "high_price", "low_price"]

    def __init__(self, name, ipo: float):
        self.name = name
        self.open_price = ipo
        self.current_price = ipo
        self.high_price = ipo
        self.low_price = ipo

    def set_open_price(self, other_price: float) -> None:
        self.open_price = other_price

    def update_prices(self, other_price: float) -> None:
        self.current_price = other_price

        if other_price > self.high_price:
            self.high_price = other_price
        elif other_price < self.low_price:
            self.low_price = other_price

    def get_name(self) -> str:
        return self.name

    def get_open_price(self) -> float:
        return self.open_price
    
    def get_current_price(self) -> float:
        return self.current_price
    
    def get_high_price(self) -> float:
        return self.high_price
    
    def get_low_price(self) -> float:
        return self.low_price
    
    def __repr__(self) -> str:
        return self.name + " @ $" + str(round(self.current_price, 2))
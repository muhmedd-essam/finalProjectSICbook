import tkinter as tk
import random
class SnakeGame:
    def __init__(self,root):
        self.root = root
        self.canvas_width = 400
        self.canvas_height = 400
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

        self.snake_size = 20
        self.snake_color = "green"
        self.snake = [(100, 100), (80, 100), (60, 100)]
        self.direction = "Right"

        self.food_size = 20
        self.food_color = "red"
        self.food = self.create_food()

        self.score = 0
        self.score_label = tk.Label(self.root, text="Score: 0")
        self.score_label.pack()

        self.delay = 100
        self.root.bind("<Key>", self.change_direction)

        self.move_snake()

    def create_food(self):
        x = random.randint(1, (self.canvas_width - self.food_size) // self.food_size) * self.food_size
        y = random.randint(1, (self.canvas_height - self.food_size) // self.food_size) * self.food_size
        food = self.canvas.create_rectangle(x, y, x + self.food_size, y + self.food_size, fill=self.food_color)
        return food

    def move_snake(self):
        head_x, head_y = self.snake[0]

        if self.direction == "Right":
            head_x += self.snake_size
        elif self.direction == "Left":
            head_x -= self.snake_size
        elif self.direction == "Up":
            head_y -= self.snake_size
        elif self.direction == "Down":
            head_y += self.snake_size

        self.snake.insert(0, (head_x, head_y))

        self.canvas.delete("snake")
        for segment in self.snake:
            x, y = segment
            self.canvas.create_rectangle(x, y, x + self.snake_size, y + self.snake_size, fill=self.snake_color,
                                         tags="snake")

        if self.check_collision():
            self.game_over()

        if self.check_food_collision():
            self.score += 10
            self.score_label.config(text="Score: {}".format(self.score))
            self.canvas.delete(self.food)
            self.food = self.create_food()
        else:
            self.snake.pop()

        self.root.after(self.delay, self.move_snake)

    def change_direction(self, event):
        key = event.keysym

        if (key == "Right" or key == "Left") and self.direction != "Right" and self.direction != "Left":
            self.direction = key
        elif (key == "Up" or key == "Down") and self.direction != "Up" and self.direction != "Down":
            self.direction = key

    def check_collision(self):
        head_x, head_y = self.snake[0]

        if (
                head_x < 0 or
                head_x >= self.canvas_width or
                head_y < 0 or
                head_y >= self.canvas_height or
                (head_x, head_y) in self.snake[1:]
        ):
            return True
        return False

    def check_food_collision(self):
        head_x, head_y = self.snake[0]
        food_x, food_y, _, _ = self.canvas.coords(self.food)

        if head_x == food_x and head_y == food_y:
            return True
        return False

    def game_over(self):
        self.canvas.delete("all")
        self.canvas.create_text(
            self.canvas_width / 2,
            self.canvas_height / 2,
            text="Game Over!",
            font=("Helvetica", 24),
            fill="red"
        )




root = tk.Tk()
root.title("Snake Game")

game = SnakeGame(root)

root.mainloop()

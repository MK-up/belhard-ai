import matplotlib.pyplot as plt

# Нарисовать гистограмму по колонке из DataFrame
def show_histogram(df, column):

    plt.hist(df[column], bins=10)  #
    plt.xlabel('X axis label')
    plt.ylabel('Y axis label')
    plt.title('Histogram of Column')
    plt.show()

# Нарисовать линейный график по двум колонкам из DataFrame
def show_line_chart(df, column_X, column_Y):

    plt.plot(df[column_X], df[column_Y], marker='o', color='b', linestyle='-')
    # Украшаем график
    plt.title('График значений по времени')
    plt.xlabel(column_X)
    plt.ylabel(column_Y)
    plt.grid(True)
    plt.show()



"""
class VisualizationManager:
    def __init__(self):
        self.visualizations = []

    def add_histogram(self, data):
        visualization = create_histogram(data)
        self.visualizations.append(visualization)

    def add_line_chart(self, data):
        visualization = create_line_chart(data)
        self.visualizations.append(visualization)

    def add_scatter_plot(self, data):
        visualization = create_scatter_plot(data)
        self.visualizations.append(visualization)

    def remove_visualization(self, visualization):
        if visualization in self.visualizations:
            self.visualizations.remove(visualization)
        else:
            print("Visualization not found.")

"""
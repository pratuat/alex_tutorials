# %%
import matplotlib.pyplot as plt
#%%

# point_1 = (1, 3)
# point_2 = (3, 9)
# point_3 = (5, 15)


# list of x-coordinates
x = [1, 3, 5]
# list of y-coordinates
y = [3, 8, 15]


# %%

# Scatter Plots
plt.scatter(x, y)

# %%

plt.plot(x, y, color="green", marker='o', markerfacecolor="red")





# %%

list_of_x = [-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

list_of_y_linear = []
list_of_y_parabolic = []

# for loop fetch values of a list one at a time.
for x in list_of_x:
    # function of a straight line
    y_linear =  3 * x + 4

    # function of a parabola
    y_parabolic = x * x

    list_of_y_linear.append(y_linear)
    list_of_y_parabolic.append(y_parabolic)


print(list_of_x)
print(list_of_y_linear)
print(list_of_y_parabolic)
# %%

plt.plot(list_of_x, list_of_y_linear, color="green")
plt.plot(list_of_x, list_of_y_parabolic, color="red")
plt.grid(True)
plt.show()

# %%

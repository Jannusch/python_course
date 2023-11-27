import matplotlib.pyplot as plt

# Create a figure (like the canvas)
fig = plt.figure()

# Create an axes object
ax = fig.subplots()
# Plot some data
ax.plot([1, 2, 3, 4], [0, 0.5, 1, 0.2])
# Save the figure to a file
fig.savefig("/workspaces/python_course/slides/week_five/figures/example_1.pdf")

# Add some text to the figure
# notice the difference between fig and ax
fig.suptitle('Explicit Interface Example')
ax.set_xlabel('x label')
ax.set_ylabel('y label')
fig.legend(['A simple line'])

fig.savefig("/workspaces/python_course/slides/week_five/figures/example_2.pdf")


# Add another line and a second legend
ax.plot([1, 2, 3, 4], [1, 3, 1, 4], 'r--')
# Now we add the legend to the axes (not the figure)
ax.legend(['A simple line', 'Another line'])

# And save the figure again
fig.savefig("/workspaces/python_course/slides/week_five/figures/myplot.pdf")



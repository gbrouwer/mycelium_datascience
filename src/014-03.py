import numpy as np

def gradient_descent(X_train,X_test,y_train,y_test):

	# If X_train and X_test do not have a constant column as a bias, add one.
	B_train = np.ones((X_train.shape[0],1))
	B_test = np.ones((X_train.shape[0],1))
	X_train = np.hstack((X_train,B_train))
	X_test = np.hstack((X_test,B_test))

	# Get and parameters
	no_regressors = X_train.shape[1]
	no_training_examples = X_train.shape[0]
	learning_rate = 0.001
	no_iterations = 100
	loss_history = []

	# Init Weights with small random weights theta.
	# Making theta a nx1 matrix makes operating on it much easier.
	theta = np.random.random((no_regressors,1)) * 0.01

	# Loop through the maximum iterations
	for i in range(no_iterations):

		# Compute the y_pred using theta and X_train
		y_pred = np.dot(X_train,theta)

		# Compute the error
		error = y_train - y_pred

		# Compute the loss
		loss = np.sum(error**2) / no_training_examples

		# Combine gradient and error and normalize
		G = np.dot(X_train.T, error) * (-2/X_train.shape[0])

		# Update the weights
		theta = theta - (G * learning_rate)

		# Store loss for plotting purposes
		loss_history.append(loss)


if __name__ == '__main__':

	X_train = np.random.random((1000,10))
	X_test = np.random.random((1000,10))
	y_train = np.random.random((1000,1))
	y_test = np.random.random((1000,1))
	gradient_descent(X_train, X_test, y_train, y_test)

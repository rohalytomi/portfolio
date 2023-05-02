import numpy as np

def cov_mat (stA, stB):
    a=np.zeros((2,2))
    a[0,0]=stA*stA
    a[1,0]=stA*stB
    a[0,1]=stB*stA
    a[1,1]=stB*stB
    return a
stA=0.3
stB=0.2
cov=cov_mat(stA,stB)


def covariance_matrix(correlation, stdevA, stdevB):
    # Calculate covariance
    covariance = correlation * stdevA * stdevB

    # Create the covariance matrix
    cov_matrix = np.array([[stdevA ** 2, covariance], [covariance, stdevB ** 2]])

    return cov_matrix
correlation = 0.7
stdevA = 1.5
stdevB = 2.0

cov_matrix = covariance_matrix(correlation, stdevA, stdevB)
print(cov_matrix)


def generate_returns(cov_matrix, means, num_returns):
    # Generate multivariate normal returns
    returns = np.random.multivariate_normal(means, cov_matrix, size=num_returns)

    return returns
cov_matrix = np.array([[2.25, 2.1], [2.1, 4.0]])
means = np.array([0.05, 0.03])
num_returns = 1000

returns = generate_returns(cov_matrix, means, num_returns)
print(returns)

sample_mean = np.mean(returns, axis=0)
sample_stdev = np.std(returns, axis=0)

print("Sample mean:", sample_mean)
print("Sample standard deviation:", sample_stdev)

sample_cov_matrix = np.cov(returns, rowvar=False)

print("Sample covariance matrix:")
print(sample_cov_matrix)






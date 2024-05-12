from setuptools import setup, find_packages

setup(
    name='LoanPrediction',
    version='1.0',
    author='Dinuwan Fernando',
    author_email='your.email@example.com',
    description='A machine learning application for predicting loan eligibility based on user data.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/dinuwanfernando/10822750-final-year-project',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'pandas',
        'numpy',
        'matplotlib',
        'scikit-learn',
        'xgboost',
        'fbprophet',  # Assuming Prophet is needed, adjust if you use `prophet` from another source
        'jupyter',   # Only if users need to run Jupyter notebooks
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  # Make sure the license matches your project's license
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.8',
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'loan_predictor=loan_prediction_version2:main',  # Adjust accordingly if you have a specific script to run
        ],
    }
)

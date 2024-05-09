from setuptools import setup, find_packages

setup(
    name='loan_prediction_gui',
    version='1.0',
    author='Your Name',
    description='A GUI application for predicting loan status.',
    packages=find_packages(),
    py_modules=['loan_prediction_version2'],
    install_requires=[
        'pandas',
        'scikit-learn',
        'xgboost',
        'statsmodels'
        'prophet'
        'matplotlib'
        'joblib'
        # Add any other dependencies here
    ],
    entry_points={
        'console_scripts': [
            'loan_prediction_version2=loan_prediction_version2:main'
        ]
    },
)

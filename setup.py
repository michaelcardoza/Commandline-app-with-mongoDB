from setuptools import setup


setup(
    name='app',
    version='0.1',
    py_modules=['app'],
    install_requires=['click'],
    entry_points=""" 
        [console_scripts]
        app=app:cli 
    """
)

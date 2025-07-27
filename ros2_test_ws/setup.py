from setuptools import find_packages, setup

package_name = 'ros2_test_ws'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros2',
<<<<<<< HEAD
    maintainer_email='johndoe123@gmail.com',
=======
    maintainer_email='venugopal.reddy.kollan@gmail.com',
>>>>>>> 8db777adc051027818bd47f9119b0335562b321e
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)

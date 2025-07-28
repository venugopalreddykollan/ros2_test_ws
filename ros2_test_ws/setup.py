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
    maintainer='venugopal reddy kollan',
    maintainer_email='venugopal.reddy.kollan@gmail.com',
    description='Ros2 package for checking the demo node and check for docker functionality',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            "test=ros2_test_ws.test:main",
        ],
    },
)
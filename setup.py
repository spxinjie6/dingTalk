from setuptools import setup, find_packages

with open("READ_ME.TXT", "r") as fh:
    long_description = fh.read()

setup(
    name="ding-talk-wb",
    version='0.0.2',
    author='spxinjie6',
    author_email='1311855817@qq.com',
    url='https://github.com/spxinjie6/dingTalk.git',
    description='Reseal DingDing Talk',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    keywords=['dingding', 'ding-talk'],
    include_package_data=True,
    zip_safe=False,
    package_dir={'': 'src'},
    packages=find_packages('src'),
    install_requires=["http"]
)

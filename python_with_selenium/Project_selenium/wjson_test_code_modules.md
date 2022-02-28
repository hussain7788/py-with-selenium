ECHO is on.
# create a new virtual environment - wjenv and activate it

cd
cd pkgs
virtualenv wjenv
source ~/pkgs/wjenv/bin/activate

# Create an alisa for wjenv (like pyenv)

# Install the following python packages

pip install selenium==4.0.0.a7
pip install pandas
pip install lxml
pip install webdrivermanager
pip install pytest
pip install typing_extensions

# Then commands to run

sudo `which webdrivermanager` chrome --linkpath /usr/local/bin 
# Automatically installs and configures chrome webdriver that matches your chrome browser version
===================================================================================================================

# How to use run.json
    config_path: This is the absolute path to the foer that contains all the config files
    output_path: This is the absolute path to the location the code should generate
    submodule_name: This is the python module that all the code will be generated in
    extend_data_gen: This is a boolean variable that tells the compiler whether to generate objects tracking code

# Commands to generate code for example site
    Go one step into the top-level repository folder, so for example if I cloned my repository in my home direction, I would do cd ~/webjson/
    Then run the following command: sudo ./webjson1.0.0.exe cpa_pm/run.json
    This is will generate the code in the example_website directory with the submodule "app"

# ECS-171-Project Web Application Usage/Installation
Heart Disease Risk Model + Calculator

### Before Installation
Please note that there is a LIVE version of our webapp hosted by Streamlit that can be located here:
https://hdmodel.streamlit.app/

This is the version we used for our project demonstration. It is hosted from a separate repository for organizational purposes, but the ``webapp.py`` and ``.pkl`` files are identical to their counterparts on the repository linked in the report. That repository can be accessed by clicking the small GitHub icon in the top right corner. Streamlit hosts their webapps directly from repositories.

### Setup
If you'd still like to run the webapp yourselves, here are the instructions:
1. Install Streamlit with ``pip install streamlit``. This installation can be verified with the command ``streamlit hello``. Streamlit seems to require Python 3.10+, otherwise some of its dependencies related to TensorFlow will not install properly.
2. If you have rerun our model generation code in the ``.ipynb`` file, you may need to downgrade Numpy to v1.24.1 with ``pip install numpy==1.24.1`` and rerun it again, as the newest version does not properly pickle MLP Classifier models due to a bug in their interaction with the random_state_() function.
3. Navigate to the directory with our ``webapp.py`` file and run the command ``streamlit run webapp.py``. This should launch a local version of the webapp!

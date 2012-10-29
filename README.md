Internal API for launching and provisioning EC2 instances
================
[API Documentation](http://btburke.github.com/launch-provision/)

To run server:
gunicorn -k egg:gunicorn#tornado internalserver:app 
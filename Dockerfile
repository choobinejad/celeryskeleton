FROM python:onbuild

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python"]


ADD run.py


CMD [ "python", "./celeryskeleton/run.py" }
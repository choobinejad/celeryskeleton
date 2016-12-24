FROM python:onbuild

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["python"]


CMD [ "python", "./celeryskeleton/run.py" }
<!--1. make sure docker && docker comose install  -->
<!-- first. build docker｜ Docker V2 version-->
docker compose up -d --build
docker compose up -d --build --remove-orphans
<!-- run docker-->
docker compose up -d

add app command:
django-admin startapp MODULE_NAME


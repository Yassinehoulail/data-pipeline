<!-- entrer dans PostgreSQL à l’intérieur du container -->
docker exec -it delivery-postgres psql -U postgres -d delivery_db

mdp:ton_mot_de_passe


docker compose logs airflow | Select-String "Password for user"
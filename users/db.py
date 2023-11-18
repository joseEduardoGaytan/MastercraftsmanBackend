from tortoise import Tortoise, run_async
from dotenv import dontenv_values

#TODO crate db_url from .env files
config = dotenv_values("users.env")

async def init():    
    await Tortoise.init(
        db_url=config['DB_URL'],
        modules={'models': ['models']}
    )

    # Generate the schema
    await Tortoise.generate_schemas()    
run_async(init())


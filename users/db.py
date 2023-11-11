from tortoise import Tortoise, run_async
#TODO crate db_url from .env files
async def init():    
    await Tortoise.init(
        db_url='mysql://master:craft@db:3306/demo',
        modules={'models': ['models']}
    )

    # Generate the schema
    await Tortoise.generate_schemas()    
run_async(init())


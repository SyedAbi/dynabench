# Copyright (c) Facebook, Inc. and its affiliates.
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

from app.api.endpoints import model
from fastapi import FastAPI
from mangum import Mangum


app = FastAPI()

app.include_router(model.router, prefix="/model", tags=["model"])


@app.get("/")
def read_root():
    return {"Hello": "Welcome to the dynalab 2.0"}


handler = Mangum(app)

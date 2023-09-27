db.createUser(
    {
        user: "admin",
        pwd: "testadmin",
        roles: [
            {
                role: "readWrite",
                db: "xpayback"
            }
        ]
    }
);
db.createCollection("xpayback");
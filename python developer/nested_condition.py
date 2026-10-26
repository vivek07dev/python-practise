student = {
    "name": "vivek",
    "address": {
        "city": "Delhi",
        "state": "DL"
    }
}

student["address"]["city"] = "gaziyabad"
student["address"].update({
    "pincode": 110001
})

print(student)
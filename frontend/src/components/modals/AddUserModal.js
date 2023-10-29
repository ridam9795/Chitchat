import React, { useRef, useState } from "react";
import axios from "axios";
import { useToast } from "@chakra-ui/react";
function AddUserModal() {
  const phoneNumber = useRef();
  const [searchedUser, setSearchedUser] = useState();
  const toast = useToast();

  const handleUserSearch = async () => {
    console.log(phoneNumber.current.value);
    const phone_number = phoneNumber.current.value;
    try {
      const { data } = await axios.get(
        "searchUser/?phone_number=" + phone_number
      );
      if (data) {
        console.log("user: ", data.user);
        setSearchedUser(data.user);
      }
    } catch (error) {
      toast({
        title: "User does not exists",
        description: error.response.data.message,
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });
    }
  };
  return (
    <>
      <button
        type="button"
        className="btn btn-primary mt-3"
        data-bs-toggle="modal"
        data-bs-target="#addUserModal">
        Add New User
      </button>

      <div
        className="modal fade"
        id="addUserModal"
        tabIndex="-1"
        aria-labelledby="exampleModalLabel"
        aria-hidden="true">
        <div className="modal-dialog">
          <div className="modal-content">
            <div className="modal-header">
              <h1 className="modal-title fs-5" id="exampleModalLabel">
                Add New User
              </h1>
              <button
                type="button"
                className="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"></button>
            </div>
            <div className="modal-body">
              <div className="input-group mb-3">
                <input
                  type="text"
                  className="form-control w-75 mr-3"
                  aria-label="Sizing example input"
                  aria-describedby="inputGroup-sizing-default"
                  placeholder="Search user with mobile number"
                  maxLength={"10"}
                  ref={phoneNumber}
                />
                <button className="btn btn-primary" onClick={handleUserSearch}>
                  search
                </button>
              </div>
              {searchedUser ? (
                <div class="card bg-light">
                  <div class="card-body">
                    <h5 class="card-title">{searchedUser.first_name}</h5>
                    <h6 class="card-subtitle mb-2 text-muted">
                      {searchedUser.phone_number}
                    </h6>
                  </div>
                </div>
              ) : (
                <></>
              )}
            </div>
            <div className="modal-footer">
              <button
                type="button"
                className="btn btn-secondary"
                data-bs-dismiss="modal">
                Close
              </button>
              <button type="button" className="btn btn-primary">
                Add User
              </button>
            </div>
          </div>
        </div>
      </div>
    </>
  );
}

export default AddUserModal;

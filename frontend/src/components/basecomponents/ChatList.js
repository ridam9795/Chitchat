import React from "react";
import AddUserModal from "../modals/AddUserModal";
import AddGroupModal from "../modals/AddGroupModal";

export default function ChatList() {
  return (
    <div className="bg-light vh-100 ">
      <div className="d-flex justify-content-center mt-1">
        <AddUserModal />
        <AddGroupModal />
      </div>
    </div>
  );
}

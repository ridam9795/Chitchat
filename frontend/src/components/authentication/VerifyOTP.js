import React, { useEffect, useState } from "react";
import { ChatState } from "../../Context/ChatProvider";
import {
  Box,
  Button,
  Container,
  FormControl,
  FormLabel,
  Input,
  Text,
  useToast,
} from "@chakra-ui/react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
function VerifyOTP() {
  const toast = useToast();
  const navigate = useNavigate();
  const { phone, setPhone } = ChatState();
  const [otp, setOtp] = useState();
  useEffect(() => {
    if (!phone) {
      navigate("/");
    }
  });
  console.log("current phone number ", phone);
  const verify_otp = async () => {
    try {
      console.log("phone number ", phone);
      const data = await axios.post("verify_otp/", {
        phone_number: phone,
        otp: otp,
      });
      console.log(data);
      toast({
        title: "OTP verified successfully",
        status: "success",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });

      navigate("/");
    } catch (error) {
      toast({
        title: "Error Occured!",
        status: "error",
        duration: 5000,
        isClosable: true,
        position: "bottom",
      });
    }
  };

  return (
    <Container maxW="xl" centerContent>
      <Box
        d="flex"
        justifyContent="center"
        p={3}
        bg="white"
        w="100%"
        m="40px 0 15px 0"
        borderRadius="lg"
        borderWidth="1px">
        <FormControl id="phone" isRequired>
          <FormLabel>Verify OTP</FormLabel>
          <Input
            placeholder="Enter OTP"
            onChange={(e) => setOtp(e.target.value)}
            maxLength={"10"}
          />
        </FormControl>
        <Button
          colorScheme="blue"
          width="100%"
          style={{ marginTop: 15 }}
          onClick={verify_otp}>
          Verify otp
        </Button>
      </Box>
    </Container>
  );
}

export default VerifyOTP;

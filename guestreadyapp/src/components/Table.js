import React, { useState, useEffect } from "react";
import axios from "axios";

const BOOKING_URL = "http://127.0.0.1:8000/booking/bookingview";
const Table = () => {
    const [errMsg, setErrMsg] = useState("");
    const [repo, setRepo] = useState([]);
    const getBookings = () => {
        axios.get(BOOKING_URL, {
            headers: {
              "Content-Type": "application/json"
            },
          })
          .then((response) => {
            const BookingData = response.data.data;
            console.log(BookingData);
            setRepo(BookingData);
          })
          .catch((err) => {
            if (!err?.response) {
              setErrMsg("No server response");
            } else if (err.response?.status === 400) {
              setErrMsg(
                "Error fetching bookings from server. Please try again"
              );
            }  else {
              setErrMsg("Something went wrong. Please try again");
            }
          });
      };
    
      useEffect(() => {
        getBookings();
      }, []);
  return (
    <table className="table">
  <thead>
    <tr>
      <th scope="col">#</th>
      <th scope="col">Flat Name</th>
      <th scope="col">Booking ID</th>
      <th scope="col">Check In</th>
      <th scope="col">Check Out</th>
      <th scope="col">Previous Booking ID</th>
    </tr>
  </thead>
  <tbody>
  {repo.map((item, index) => (
            <tr key={index}>
              <th scope="row">{index + 1}</th>
              <td>{item.flatname}</td>
              <td>{item.id}</td>
              <td>{item.checkin}</td>
              <td>{item.checkout}</td>
              <td>{item.previous_booking_id}</td>
            </tr>
          ))}
  </tbody>
</table>
  )
}

export default Table
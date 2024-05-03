const IsBusinessOpen = () => {
  const workHours = "08:00AM-09:00PM";

  if (workHours === "Closed") {
    return "Closed";
  }

  const [openTimeStr, closeTimeStr] = workHours.split("-");

  const currentTime = new Date();
  const currentHour = currentTime.getHours();
  const currentMinute = currentTime.getMinutes();

  const [openHour, openMinute] = parseTime(openTimeStr);
  const [closeHour, closeMinute] = parseTime(closeTimeStr);

  const isOpen =
    (currentHour > openHour ||
      (currentHour === openHour && currentMinute >= openMinute)) &&
    (currentHour < closeHour ||
      (currentHour === closeHour && currentMinute < closeMinute));

  return isOpen ? "Open" : "Closed";
};

function parseTime(timeStr) {
  const [time, period] = timeStr.split(/([AP]M)/);
  let hour = parseInt(time, 10);
  if (period === "PM" && hour !== 12) {
    hour += 12;
  } else if (period === "AM" && hour === 12) {
    hour = 0;
  }
  const minute = parseInt(time.split(":")[1], 10);
  return [hour, minute];
}

console.log("Duration: ", IsBusinessOpen());

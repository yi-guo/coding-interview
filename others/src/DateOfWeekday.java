public class DateOfWeekday {

    /**
     * Write a function that, given a date and a weekday, returns the date of that weekday relative to the given date.
     *
     * A date is an integer, being the number of days since January 1, 1984 (a Sunday).
     * A weekday is an integer representing a day of the week, in the future or the past, where
     *   - 1 means the following Monday, 2 means the following Tuesday, etc., through 7 for following Sunday; and 8
     *     means Monday after following, and so on;
     *   - 0 means the given date;
     *   - -1 means the preceding Monday, -2 means the preceding Tuesday, etc., through -7 for preceding Sunday, -8 for
     *     Monday before preceding, and so on.
     *
     * For example, given a date 11111 that falls on a Tuesday,
     *   [11111, 0] => 11111 (Same day)
     *   [11111, 1] => 11117 (Following Monday)
     *   [11111, 3] => 11112 (Following Wednesday)
     *   [11111, -7] => 11109 (Preceding Sunday)
     *   [11111, -3] => 11105 (Preceding Wednesday)
     *   [11111, -1] => 11110 (Preceding Monday)
     */

    public static void main(String[] args) {
        System.out.println(dateOfWeekday(11113, 1));
    }

    public static int dateOfWeekday(int date, int weekday) {
        if (weekday == 0)
            return date;
        int dayOfDate = date % 7;
        int numOfWeeks = weekday / 7;
        weekday = weekday % 7;
        if (weekday > 0) {
            if (weekday > dayOfDate)
                date = date + weekday - dayOfDate;
            else
                date = date + 7 - dayOfDate + weekday;
        } else {
            if (Math.abs(weekday) < dayOfDate)
                date = date - dayOfDate - weekday;
            else
                date = date - 7 - dayOfDate - weekday;
        }
        return date + numOfWeeks * 7;
    }

}

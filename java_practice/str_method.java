package Java;

public class str_method {
    public static void main(String[] args){
        String str = "hello";
        String str2 = "rrrr";
        String str4 = "   444   3r   ";
        String intStr ="333";

        //길이 반환
        System.out.println(str.length());
        //빈 문자열 체크
        System.out.println(str.isEmpty());
        System.out.println(str4.isEmpty());
        //문자 찾기
        System.out.println("문자열 찾기");
        System.out.println(str.indexOf(3));
        System.out.println(str.indexOf("l"));
        System.out.println(str.charAt(3));
        System.out.println(str.lastIndexOf("l"));
        //문자 자르기
        System.out.println(str.substring(1,4));
        //문자 치환
        System.out.println(str.replace("l","klkk"));
        String str3 = str2.replace("r", "klklklkl");
        //모든 문자 치환
        System.out.println(str3.replaceAll(".","k"));
        //첫문자 치환
        System.out.println(str.replaceFirst("l","k"));
        //문자 동일 여부
        System.out.println(str.equals(str3));
        //문자 비교
        System.out.println(str.compareTo(str3));
        //문자 포함 여부
        System.out.println("문자열 포함 여부");
        System.out.println(str.contains("t"));
        System.out.println(str.contains("l"));
        //문자열 분리
        System.out.println(str.split("l")[0]); //String[] 배열로 반환
        for (String string : str.split("")) {
            System.out.println(string);
        }
        //문자 앞 뒤 공백 제거
        System.out.println(str4.trim());

        //문자 숫자 변환
        int kkk = Integer.parseInt(intStr);
        String olk = Integer.toString(kkk);
        System.out.println(kkk + olk);


        // 스트링 빌더 메소드
        StringBuilder sb = new StringBuilder();
        // 문자열 추가
        sb.append("hello");
        //특정 인덱스 문자 삽입
        sb.insert(1, "ko");
        System.out.println(sb);
        //문자열 삭제
        System.out.println("문자열 삭제");
        System.out.println(sb);
        System.out.println(sb.delete(1,2));
        System.out.println(sb.deleteCharAt(3));

        System.out.println(sb);
        //특정 인덱스 문자 삭제

        //특정 인덱스 문자 변경
        System.out.println(sb.replace(1,2,"k"));
        //문자열 뒤집기
        System.out.println(sb.reverse());

        //문자열 길이 줄이기
        sb.setLength(2);
        System.out.println(sb);
        //문자열 절대 길이 늘이기
        sb.setLength(8);
        System.out.println(sb);
        String sbToStr = sb.toString();

        System.out.println(sbToStr);
    }
}

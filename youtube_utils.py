from urllib.parse import urlparse, parse_qs
from youtube_transcript_api import YouTubeTranscriptApi


def get_video_id_from_url(url: str) -> str:
    """
    Extract the youtube video id from given youtube link

    @params
    url: Youtube video link

    @return
    video id
    """
    url_chunks = urlparse(url)
    if not url_chunks.query:
        video_id = url_chunks.path.split("/")[-1]
        return video_id

    video_id = parse_qs(url_chunks.query).get("v", [""])[0]

    if not video_id:
        video_id = url_chunks.path.split("/")[-1]
        return video_id

    return video_id


def get_youtube_transcript(youtube_link: str) -> str:
    """
    Extract the youtube transcrip from a given script

    @params
    youtube_link: Youtube link

    @return
    full text script
    """
    #get the video id from the link
    video_id = get_video_id_from_url(youtube_link)

    full_transcript = None

    try:
        sub_transcript = YouTubeTranscriptApi.get_transcript(video_id)
        full_transcript = " ".join([sub_content["text"] for sub_content in sub_transcript])
    except Exception as error:
        message = "cannot extract the transcript. Error: {}".format(str(error))
        print(message)
        return full_transcript

    return full_transcript
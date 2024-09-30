# import asyncio
# import face_recognition



def perform_face_recognition():
    pass
    # local_csv_path = './images'




    # chunk_size = 100
    #
    # for chunk_index, batch_df in fetch_data_in_chunks(local_csv_path, chunk_size):
    #     process_batch(batch_df)

# def fetch_data_in_chunks(file_path, chunk_size):
#     for i, chunk in enumerate(pd.read_csv(file_path, chunksize=chunk_size), 1):
#         yield i, chunk

# def process_batch(batch_df):
#     loop = asyncio.new_event_loop()  # Create a new event loop
#     asyncio.set_event_loop(loop)  # Set the new event loop as the current one
#     compare_faces(local_file_front, local_file_selfie, msisdn)

    # async def process_async(msisdn, local_file_front, local_file_selfie):
    #     await compare_faces(local_file_front, local_file_selfie, msisdn)
    #
    # async def main():
    #     tasks = []
        # for msisdn in msisdn_array:
        #     result = get_files_from_sftp(sftp, msisdn)
        #     if result is None:
        #         logger.log_message("ERROR", f"Error: get_files_from_sftp() returned None. MSISDN: {msisdn}")
        #         continue
        #     local_file_front, local_file_selfie, msisdn = result
        #     tasks.append(process_async(msisdn, local_file_front, local_file_selfie))

        # await asyncio.gather(*tasks)

    # loop.run_until_complete(main())  # Run the main coroutine within the event loop

# def compare_faces(image_front, image_selfie, msisdn):
#     try:
#         # Load images
#         front_quadrant = extract_top_left_quadrant(image_front)
#         if front_quadrant is not None:
#             selfie = face_recognition.load_image_file(image_selfie)
#             selfie_locations = face_recognition.face_locations(selfie)
#             save_face(selfie, selfie_locations, f"{app_config._image_output_base_dir}/{msisdn}",
#                       f"{msisdn}-selfie-photo")
#             SCORE = Hauwei.process_similarity(image_front, image_selfie)
#             if SCORE is None:
#                 STATUS = NOT_MATCHED
#                 SCORE = 0
#             else:
#                 STATUS = MATCHED if SCORE >= app_config._selfie_threshold else NOT_MATCHED
#                 logger.log_message("INFO", f"Msisdn: {msisdn} , SCORE: {SCORE}, STATUS: {STATUS}")
#
#             Process.remove_folder([app_config._image_output_base_dir+'/'+str(msisdn)])
#             await psqlKycDataSourceConfig.update_score_subscriber(str(msisdn), STATUS, SCORE)
#     except Exception:
#         logger.log_message("ERROR", f"File for {msisdn} front image can not load from local.")
#         pass